import socket
import json
import math

class RPCServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.func_map = {
            "floor": self._floor,
            "nroot": self._nroot,
            "reverse": self._reverse,
            "validAnagram": self._validAnagram,
            "sort": self._sort,
        }
        self.client_sockets = {}  # クライアントソケットを管理

    def _floor(self, x):
        return math.floor(x)

    def _nroot(self, n, x):
        return x ** (1 / n)

    def _reverse(self, s):
        return s[::-1]

    def _validAnagram(self, str1, str2):
        return sorted(str1) == sorted(str2)

    def _sort(self, strArr):
        return sorted(strArr)

    def _execute_rpc(self, request):
        try:
            method = request["method"]
            params = request["params"]
            param_types = request["param_types"]
            request_id = request["id"]

            if method not in self.func_map:
                raise ValueError("Method not found")

            func = self.func_map[method]

            # パラメータの型検証
            if len(params) != len(param_types):
                raise ValueError("Parameter count mismatch")

            typed_params = []
            for param, param_type in zip(params, param_types):
                if param_type == "int":
                    typed_params.append(int(param))
                elif param_type == "double":
                    typed_params.append(float(param))
                elif param_type == "string":
                    typed_params.append(str(param))
                elif param_type == "string[]":
                    typed_params.append(param)
                else:
                    raise ValueError(f"Invalid parameter type: {param_type}")
            
            result = func(*typed_params)
            response = {
                "results": result,
                "result_type": str(type(result).__name__),
                "id": request_id,
            }
            return response

        except Exception as e:
            return {"error": str(e), "id": request["id"]}

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            print(f"Server listening on {self.host}:{self.port}")

            while True:
                client_socket, addr = s.accept()
                print(f"Connected by {addr}")
                self.client_sockets[addr] = client_socket # クライアントソケットを管理

                self.handle_client(client_socket)

    def handle_client(self, client_socket):
      while True:
          data = client_socket.recv(1024)
          if not data:
              break

          request = json.loads(data.decode())
          response = self._execute_rpc(request)
          client_socket.sendall(json.dumps(response).encode())

      client_socket.close()
      print("Client disconnected")

if __name__ == "__main__":
    server = RPCServer("127.0.0.1", 65432)
    server.start()