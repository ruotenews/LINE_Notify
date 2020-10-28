from bs4 import BeautifulSoup


class Utils:
    @staticmethod
    def get_divs_by_class(html: str, class_: str) -> list:
        soup = BeautifulSoup(html, "html.parser")
        return [element for element in soup.find_all("div", attrs={"class": class_})]
