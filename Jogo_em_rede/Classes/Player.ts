
class Player {
    name : string;
    guesses : string; //  as letras que foram adivinhadas pelo jogador.

    constructor(name: string , guesses: string) {
        this.name = name
        this.guesses = guesses
    }

    //permite que o jogador faça uma tentativa de adivinhar a letra.
    makeGuess(letter: string): void {

    }

}