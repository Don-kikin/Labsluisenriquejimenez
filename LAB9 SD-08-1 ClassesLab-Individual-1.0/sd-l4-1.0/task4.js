export class Player {
  constructor(player, level) {
    this.name = player;
    this.level = level;
  }
  
  info() {
    return this.name + ' has reached Level ' + this.level + '!';
  }
  levelUp(){
    this.level += 1;
  }
}