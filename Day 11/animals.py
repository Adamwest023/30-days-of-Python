class Animal:
    noise = "Rrr"
    color = "Red"
    def make_noise(self):
        print(f"{self.noise}")
    def set_noise(self, new_noise):
        self.noise = new_noise
        
    def get_noise(self):
        return self.noise
    def set_noise(self):
        self.new_noise = new_noise
        return self.noise

    def get_color(self):
        return self.color
    def set_color(self):
        self.new_color = new_color
        return self.color
        
class Wolf(Animal):
    noise = "grrr"
    

class BabyWolf(Wolf):
    color = "yellow"