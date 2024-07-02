package main

import (
	"fmt"
	"sync"
)

func main() {
	var wg sync.WaitGroup

	// Create actors
	actor1 := NewActor(1, &wg)
	actor2 := NewActor(2, &wg)

	// Add actors to the wait group
	wg.Add(2)

	// Start actors
	actor1.Start()
	actor2.Start()

	// Send initial messages
	actor1.Send(Message{content: "Hello Actor 2", sender: actor2})
	actor2.Send(Message{content: "Hello Actor 1", sender: actor1})

	// Wait for all actors to finish processing
	wg.Wait()

	fmt.Println("All actors have finished processing.")
}
