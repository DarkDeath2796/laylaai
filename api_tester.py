import requests


def test_api(message: str, name: str) -> None:
    url = "http://localhost:5000/api/message"
    headers: dict[str, str] = {"Content-Type": "application/json"}
    data: dict[str, str] = {
        "message": message,
        "name": name
    }
    response = requests.post(url, headers=headers, json=data)
    print(f"Response: {response.status_code}, {response.text}")


def main() -> None:
    while 1:
        params: list[str] = input("Enter message and name separated by a comma: ").split(",")
        if len(params) != 2:
            print("Invalid input. Please enter message and name separated by a comma.")
            continue
        message: str = params[0]
        name: str = params[1].strip()
        test_api(message, name)
        
        
        
if __name__ == "__main__":
    main()