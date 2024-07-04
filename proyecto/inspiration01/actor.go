package main

import (
	"fmt"
	"sync"
)

// Message defines a simple message structure
type Message struct {
	content string
	sender  *Actor
}

// Actor represents a basic actor with an ID, a channel for receiving messages, and a process function
type Actor struct {
	id      int
	mailbox chan Message
	wg      *sync.WaitGroup
}

// NewActor creates a new actor with the given ID
func NewActor(id int, wg *sync.WaitGroup) *Actor {
	return &Actor{
		id:      id,
		mailbox: make(chan Message, 1), // Limit the mailbox to 1 message
		wg:      wg,
	}
}

// Send sends a message to the actor's mailbox
func (a *Actor) Send(msg Message) {
	a.mailbox <- msg
}

// Start starts the actor's message processing loop
func (a *Actor) Start() {
	go func() {
		for msg := range a.mailbox {
			fmt.Printf("Actor %d received message: %s\n", a.id, msg.content)
			a.process(msg)
			break // Exit the loop after processing one message
		}
		a.wg.Done()
	}()
}

// process defines how the actor processes incoming messages
func (a *Actor) process(msg Message) {
	// Example processing: respond back to the sender if needed
	if msg.sender != nil {
		response := Message{content: fmt.Sprintf("Hello from Actor %d", a.id), sender: a}
		msg.sender.Send(response)
	}
}
