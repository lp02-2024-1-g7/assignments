from ActorLangParserListener import ActorLangParserListener
from actor import Actor, Message
from ActorLangParser import ActorLangParser

class MyActorLangListener(ActorLangParserListener):
    def __init__(self):
        self.actors = {}  # Store created actors
        self.actions = []  # Store actions to be executed

    def enterActorDefinition(self, ctx):
        """
        This method is called when entering an actor definition in the grammar.

        Parameters:
            ctx (antlr4.ParserRuleContext): The context object representing the actor definition.

        Returns:
            None

        Side Effects:
            - Updates the `actors` dictionary with a new Actor object.

        """
        actor_id = ctx.IDENTIFIER().getText()
        port = ctx.actorBody().portDeclaration().INT_LITERAL().getText()
        new_actor = Actor(actor_id, port)
        self.actors[actor_id] = new_actor
        new_actor.send_broadcast(f'New {actor_id} Created')

    def exitSendStatement(self, ctx):
        """
        Process the exit event of the 'sendStatement' rule.

        Args:
            ctx: The context object representing the 'sendStatement' rule.

        Returns:
            None

        Raises:
            None
        """
        sender_name = ctx.IDENTIFIER().getText()
        recipient_name = ctx.STRING_LITERAL(1).getText().strip('"')
        message = ctx.STRING_LITERAL(0).getText().strip('"')
        recipient_address = ctx.STRING_LITERAL(1).getText().strip('"')
        port = ctx.INT_LITERAL().getText()  # Port number

        action = ("send", sender_name, recipient_name, message, recipient_address, port)
        self.actions.append(action)

    def exitStartStatement(self, ctx):
        """
        Starts the actor with the given identifier.

        Parameters:
        - ctx: The context object containing the actor identifier.

        Returns:
        None
        """
        actor_id = ctx.IDENTIFIER().getText()
        port = ctx.STRING_LITERAL().getText().strip('"')
        action = ("start", actor_id, port)
        self.actions.append(action)
        

    def exitPrintStatement(self, ctx):
        """
        Prints the message extracted from the given context.

        Parameters:
        - ctx: The context object containing the string literal.

        Returns:
        None
        """
        message = ctx.STRING_LITERAL().getText().strip('"')
        print(message)

    def execute_actions(self):
        for action in self.actions:
            if action[0] == "send":
                _action, sender_name, recipient_name, message, recipient_address, port = action
                sender = self.actors[sender_name]
                sender.send(recipient_address, port, message)
                print(f'Message sent to {recipient_name}')
            elif action[0] == "start":
                port = action[2]
                actor = self.actors[action[1]]
                actor.start()
                print(f'{actor} has started')
