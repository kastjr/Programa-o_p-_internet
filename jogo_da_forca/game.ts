
class game {
    private word : string;            // palavra a ser adivinhada
    private guesses : string;         // as letras que foram adivinhadas pelos jogadores
    private currentPlayer : Player;   // o jogador atual

    constructor(word : string , guesses : string , currentPlayer : Player) {
        this.word = word
        this.guesses = guesses
        this.currentPlayer = currentPlayer

    }

    // inicia o jogo, definindo a palavra a ser adivinhada e o jogador inicial.
    public startGame(): void {

    }

    //exibe o tabuleiro do jogo, com as letras adivinhadas e as partes da forca que foram desenhadas.
    public displayBoard(): void {

    }

    // permite que o jogador atual faça uma tentativa de adivinhar a letra.
    public makeGuess(letter: string): void {

    }

    //alterna entre os jogadores.
    public switchPlayer(): void {

    }


    
}