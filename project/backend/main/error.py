from flask import render_template


def erro_404(e):
    return render_template('erro-404.html')
