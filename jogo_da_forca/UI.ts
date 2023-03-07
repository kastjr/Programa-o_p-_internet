class UI {
    word: any;
    guesses: any;
    currentPlayer: any;


    displayMessage(message: string) {
        console.log(message);
      }

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

      
      getPlayerGuess(): string {
        let guess: string = '';
    
        while (!guess.match(/^[a-zA-Z]$/)) {
          guess = readline.question(`Digite uma letra: `).toLowerCase();
    
          if (!guess.match(/^[a-zA-Z]$/)) {
            console.log(`Por favor, digite apenas uma letra.`);
          }
        }
    
        return guess;
      }
}
