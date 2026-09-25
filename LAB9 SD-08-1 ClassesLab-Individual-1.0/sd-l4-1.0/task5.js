export class Player {
  constructor(player, level) {
    this.name = player;
    this.level = level;
    this.xp = 0;
    this.xpRequired = 100; // Experiencia necesaria para el siguiente nivel
  }

  info() {
    return this.name + ' has reached Level ' + this.level + '!';
  }

  gainXp(points) {
    this.xp += points;
    while (this.xp >= this.xpRequired) {
      this.xp -= this.xpRequired; 
      this.level += 1;
    }
  }
}