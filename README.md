# Resumo
O intuito do projeto é criar um chat usando a biblioteca flet. No momento está em funcionamento apenas local, porém futuramente serão feitas melhorias visuais e deixa-lo disponível através de um link. Basicamente a pessoa entra no site, informa o nome e entra no chat, podendo enviar mensagem e conversar com outra pessoa que também logar. 
## Funcionamento
- Criar a função main (onde ficará todas as informações do site) e criar a coluna onde o titulo irá aparecer;
- Criar um botão (ElevatedButton) que será onde o usuário irá clicar para entrar no chat;  
- Fazer uma função, onde, quando o usuário clicar para iniciar o chat, abra um popup para ele informar seu nome, com um botão para entrar no chat;
- Quando algum usuário entra no chat é informado no canto superior quem entrou;
- Adicionar o método pagina.pubsub.subscribe para que toda vez que um novo usuário entre no chat seja avisado que o mesmo entrou com: pagina.pubsub.send_all(f'{nome_usuario.value} entrou no chat');
- Após isso é necessário criar o campo onde o usuário irá enviar uma mensagem;
- Seguido disso criar uma função para que, sempre que o usuário envie uma mensagem, o campo seja limpo e a mensagem digitada apareça para todos;
## Adaptações
Não é necessária nenhuma adaptação no código para que ele funcione na sua máquina, apenas alguma preferência visual ou algo do tipo.
## Observações
É importante sempre lembrar de rodar um pagina.update() toda vez que fizer uma mudança visual no site.
## Tecnologias Usadas
- flet
