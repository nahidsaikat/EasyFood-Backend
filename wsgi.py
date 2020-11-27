from easy_food import create_app

app = create_app()

if __name__ == "__main__":
    print(f' * ENV is set to "{app.config["ENV"]}"')
    app.run(host='0.0.0.0')
