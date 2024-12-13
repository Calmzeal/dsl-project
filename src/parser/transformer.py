from lark import Transformer

class DSLTransformer(Transformer):
    def start(self, items):
        return items[0]  # Return the first (and only) statement

    def statement(self, items):
        name = str(items[0])
        actions = items[1]
        return {"command": name, "actions": actions}

    def block(self, items):
        return items

    def action(self, items):
        action_type = str(items[0])
        argument = str(items[1]).strip('"')
        return {"type": action_type, "argument": argument}

    def NAME(self, token):
        return str(token)