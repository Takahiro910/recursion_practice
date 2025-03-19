const net = require("net");

function sendRPCRequest(host, port, method, params, paramTypes, requestId) {
  return new Promise((resolve, reject) => {
    const client = net.createConnection({ host: host, port: port }, () => {
      console.log("Connected to server");

      const request = {
        method: method,
        params: params,
        param_types: paramTypes,
        id: requestId,
      };

      client.write(JSON.stringify(request));
    });

    client.on("data", (data) => {
      const response = JSON.parse(data.toString());
      resolve(response);
      client.end();
    });

    client.on("end", () => {
      console.log("Disconnected from server");
    });

    client.on("error", (err) => {
        reject(err);
    })
  });
}

async function main() {
  const host = "127.0.0.1";
  const port = 65432;

  try {
    const response1 = await sendRPCRequest(host, port, "floor", [3.14], ["double"], 1);
    console.log("Response 1:", response1);

    const response2 = await sendRPCRequest(host, port, "reverse", ["hello"], ["string"], 2);
    console.log("Response 2:", response2);

    const response3 = await sendRPCRequest(host,port,"validAnagram", ["hoge","geho"],["string","string"],3);
    console.log("Response 3:", response3)

  } catch (err) {
    console.error("Error:", err);
  }
}

main();