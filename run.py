from app.app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=app.config['FLASK_PORT'],debug=True) # debug=True는 저장시 자동으로 재시작