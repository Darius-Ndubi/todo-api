from flask import Flask
from flask_restplus import Api, Resource, fields
from flask_cors import CORS

from db import FirebaseDB

app = Flask("__name__")
CORS(app)
api = Api(
    app,
    version="1.0",
    default_label="Todo API",
    default="ToDo"
)

todo = api.model(
    "Todo",
    {
        "name": fields.String(readonly=True, description="Unique identifier of todo"),
        "body": fields.String(required=True, description="name of the todo"),
        "done": fields.Boolean(default=False, description="status of the todo")
    }
)
todo_status = api.model(
    "TodoStatus",
    {
        "done": fields.Boolean(default=False, description="status of the todo")
    }
)

@api.route("/todo")
class Todos(Resource):
    """fetch todos and create todo"""

    @api.doc("fetch all todos")
    def get(self):
        """fetch all todos"""
        todos = FirebaseDB().get_todos()
        return todos, 200


    @api.doc("create a todo")
    @api.expect(todo)
    def post(self):
        """create a todo item"""
        # verify task is not empty
        if len(api.payload["body"]) == 0:
            return {
                "message": "Task should not be empty",
                "status": 400
            }, 400
        FirebaseDB().create_todo(api.payload)

        return {
            "message": "Todo created"
        }, 201

@api.route("/todo/<name>")
class Todo(Resource):

    @api.expect(todo_status)
    def put(self, name):
        """Update a todo status """
        FirebaseDB().edit_todo(
            name,
            api.payload
        )
        return {
            "message": "Todo updated!"
        }, 200


if __name__=="__main__":
    app.run(debug=False)
