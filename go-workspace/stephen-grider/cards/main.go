package main

import "fmt"

func main() {
	cards := deck{"Ace of Diamond", newCard()}
	cards = append(cards, "Six of Spades")
	for index, card := range cards {
		fmt.Println(index, card)
	}

}

func newCard() string {
	return "Five of Diamonds"
}
