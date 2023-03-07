
class game {
    private word : string;            // palavra a ser adivinhada
    private guesses : string[];        // as letras que foram adivinhadas pelos jogadores
    private currentPlayer : Player;   // o jogador atual
    player1!: Player;
    player2!: Player;

    constructor() {
        this.word = "";
        this.guesses = []
        this.currentPlayer = new Player("Player 1", ""); // Define o jogador inicial como Player 1
      }

    // inicia o jogo, definindo a palavra a ser adivinhada e o jogador inicial.
    startGame(word: string) {
        this.word = word;
        this.guesses = [];
        this.currentPlayer = new Player("Player 1", ""); // Define o jogador inicial como Player 1
        this.displayBoard();
      }

    //exibe o tabuleiro do jogo, com as letras adivinhadas e as partes da forca que foram desenhadas.
    displayBoard() {
        // Limpa a tela
        console.clear();
    
        // Exibe a palavra a ser adivinhada com as letras adivinhadas pelo jogador atual
        let displayWord = "";
        for (const letter of this.word) {
          if (this.guesses.includes(letter)) {
            displayWord += letter;
          } else {
            displayWord += "_";
          }
        }
        console.log(`Palavra: ${displayWord}`);
    
        // Exibe as partes da forca que foram desenhadas
        console.log(`  +---+
      |   |
      ${this.guesses.length >= 1 ? "|   O" : "|"}
      ${this.guesses.length >= 3 ? "|  /|\\" : this.guesses.length == 2 ? "|   |" : "|"}
      ${this.guesses.length >= 5 ? "|  / \\" : this.guesses.length == 4 ? "|  /" : "|"}
      |
    =========
    `);
    
        // Exibe a vez do jogador atual
        console.log(`Vez de ${this.currentPlayer.name}`);
      }
    

    // permite que o jogador atual faça uma tentativa de adivinhar a letra.
    makeGuess(letter: string) {
        // Verifica se a letra já foi adivinhada antes
        if (this.guesses.includes(letter)) {
          console.log("Você já tentou adivinhar esta letra antes.");
          return;
        }
    
        // Adiciona a letra às tentativas do jogador atual
        this.guesses.push(letter);
    
        // Verifica se a letra está presente na palavra
        if (this.word.includes(letter)) {
          console.log(`Parabéns! A letra "${letter}" está na palavra.`);
    
          // Verifica se o jogador atual adivinhou todas as letras da palavra
          if (this.word.split("").every((l) => this.guesses.includes(l))) {
            console.log(`Parabéns! ${this.currentPlayer.name} venceu o jogo!`);
            return;
          }
        } else {
          console.log(`A letra "${letter}" não está na palavra.`);
          this.switchPlayer(); // Alterna para o próximo jogador
        }
    
        this.displayBoard(); // Exibe o tabuleiro atualizado
      }

    //alterna entre os jogadores.
    switchPlayer() {
        if (this.currentPlayer === this.player1) {
          this.currentPlayer = this.player2;
        } else {
          this.currentPlayer = this.player1;
        }
    
        console.log(`Agora é a vez de ${this.currentPlayer.name} jogar.`);
      }


    
}
