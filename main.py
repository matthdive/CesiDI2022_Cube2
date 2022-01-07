from website import create_app


app = create_app()


# Run our Flask APP
if __name__ == '__main__':
    app.run(debug=True)