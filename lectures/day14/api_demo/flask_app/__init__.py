from flask import Flask, render_template, redirect, request, jsonify
import requests
from pprint import pprint

app = Flask(__name__)

base_url = "https://rickandmortyapi.com/api/"