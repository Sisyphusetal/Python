from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secrety_key = "Wood 5"