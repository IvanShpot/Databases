from model import Model
from view import View
from controller import Controller

prog = Controller(Model("localhost", "5432", "School", "postgres", "Pr0gr3s"), View())
prog.menu()

