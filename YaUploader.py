import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token
        self.header = {"Authorization": f"OAuth {token}"}

    # 1 получение ссылки для загрузки на Яндекс Диск
    def getDownloadLink(self):
        resp1 = requests.get("https://cloud-api.yandex.net/v1/disk/resources/upload",
                             params={"path": "/Cat.jpg", "overwrite": "true"},
                             headers=self.header)
        resp1.raise_for_status()
        data1 = resp1.json()
        href = data1["href"]
        return href

    # 2 загрузка файла на Яндекс Диск
    def upload(self, path_file):
        href = self.getDownloadLink()
        with open(path_file, "rb") as file:
            resp2 = requests.put(href, files={"file": file})
        resp2.raise_for_status()
        return resp2.status_code

token = ""

if __name__ == '__main__':
    uploader = YaUploader(f"{token}")
    result = uploader.upload("D:/Загрузки/Cat.jpg")


