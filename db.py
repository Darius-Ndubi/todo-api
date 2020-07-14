"""Module to perform db operations"""
import os

from firebase import firebase

class FirebaseDB:
    firebase_connect = firebase.FirebaseApplication(os.getenv("DB_URI"), None)
    db_path = os.getenv("DB_PATH")

    def create_todo(self, data):
        """method to create todo in the fb"""
        todo = self.firebase_connect.post(
            self.db_path,
            data
        )
        return todo

    def get_todos(self):
        """method to get all todos"""
        todos = self.firebase_connect.get(
            self.db_path,
            "")
        return todos

    def edit_todo(self, name, data):
        """method to update todo status"""
        update_todo = self.firebase_connect.put(
            self.db_path + "/" + name,
            "done",
            data["done"]
        )
        return update_todo
