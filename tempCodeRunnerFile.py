from flask import Flask, render_template, Response, jsonify
import gunicorn
from camera import *