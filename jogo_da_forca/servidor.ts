import * as net from 'net';

const server: net.Server = net.createServer((socket: net.Socket) => {
   console.log(`Cliente conectado: ${socket.remoteAddress}:${socket.remotePort}`);
   socket.write('Olá, cliente!\n');
   
   socket.on('data', (data: Buffer) => {
      console.log(`Mensagem do cliente: ${data.toString()}`);
   });

   socket.on('end', () => {
      console.log('Cliente desconectado');
   });
});

server.listen(3000, () => {
   console.log('Servidor inicializado na porta 3000');
});