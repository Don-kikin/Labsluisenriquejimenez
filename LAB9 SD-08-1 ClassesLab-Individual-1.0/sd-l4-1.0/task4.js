export class Player {
  constructor(player, level) {
    this.name = player;
    this.level = level;
    this.levelup = level + 1;
  }
  
  Info() {
    return this.name + ' has reached Level ' + this.level + '!';
  }
  Info
    return this.name + ' has reached Level ' + this.levelup + '!';
  }
}