package main

import (
	"bufio"
	"fmt"
	"net"
	"os"
	"strconv"
	"time"
)

// Message defines a simple message structure
type Message struct {
	content string
}

// Actor represents a basic actor with an ID and a port
type Actor struct {
	id   int
	port string
}

// NewActor creates a new actor with the given ID and port
func NewActor(id int, port string) *Actor {
	return &Actor{
		id:   id,
		port: port,
	}
}

// Send sends a message to another actor
func (a *Actor) Send(to string, msg Message) {
	conn, err := net.Dial("tcp", to)
	if err != nil {
		fmt.Println("Error connecting to actor:", err)
		return
	}
	defer conn.Close()
	fmt.Fprintf(conn, msg.content+"\n")
}

// Start starts the actor's server to receive messages
func (a *Actor) Start() {
	ln, err := net.Listen("tcp", a.port)
	if err != nil {
		fmt.Println("Error starting server:", err)
		return
	}
	defer ln.Close()

	for {
		conn, err := ln.Accept()
		if err != nil {
			fmt.Println("Error accepting connection:", err)
			continue
		}
		go a.handleConnection(conn)
	}
}

func (a *Actor) handleConnection(conn net.Conn) {
	defer conn.Close()
	message, err := bufio.NewReader(conn).ReadString('\n')
	if err != nil {
		fmt.Println("Error reading message:", err)
		return
	}
	fmt.Printf("Actor %d received message: %s", a.id, message)
}

func main() {
	if len(os.Args) != 3 {
		fmt.Println("Usage: go run actor.go <actor_id> <port>")
		return
	}

	actorID, err := strconv.Atoi(os.Args[1])
	if err != nil {
		fmt.Println("Invalid actor ID")
		return
	}

	port := os.Args[2]
	actor := NewActor(actorID, port)
	go actor.Start()

	if actorID == 1 {
		// Send a message to Actor 2 after a short delay to ensure Actor 2 is ready
		time.Sleep(2 * time.Second)
		actor.Send("localhost:6001", Message{content: "Hello Actor 2"})
	}

	// Keep the actor running to listen for responses
	select {}
}
