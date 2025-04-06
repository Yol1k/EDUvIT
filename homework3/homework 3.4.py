class Game:
    platform = "PC"
    isFree = False

    def __init__(self, title: str, genre: str, release_year: str, developer: str, price: float):
        self.title = title          
        self.genre = genre      
        self.release_year = release_year  
        self.developer = developer 
        self.price = price          
        self.is_installed = False
        self.is_deleted = False
        
    def __str__(self):
        return f"{self.title} ({self.release_year}) - {self.genre} by {self.developer}"

    def install(self):
        if not self.is_installed:
            self.is_installed = True
            print(f"{self.title} успешно установлена!")
        else:
            print(f"{self.title} уже установлена!")

    def delete(self):
        if self.is_deleted:
            print(f"{self.title} уже удалена!")
            return
        self.is_installed = False
        self.is_deleted = True
        print(f"{self.title} успешно удалена.")

    def play(self):
        if self.is_installed:
            return f"Запускаем {self.title}..."
        return f"Ошибка: {self.title} не установлена!"

    def get_age(self, current_year: int) -> int:
        return current_year - self.release_year
    
    def change_platform(self, platform: str) -> None:
        Game.platform = platform

game1 = Game("The Witcher 3", "RPG", 2015, "CD Projekt Red", 39.99)
game2 = Game("Counter-Strike 2", "Shooter", 2023, "Valve", 0.0)
print(game1)
print(game2)
game1.install()
game1.delete()
print(game1.play())
print(f"Возраст игры: {game2.get_age(2025)} лет")
game1.change_platform("PlayStation 5")
print(f"Платформа игры {game1.title} изменена на: {Game.platform}")
