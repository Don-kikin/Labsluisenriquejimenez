export class Player {
    constructor( Player,level ) {
      this.name = Player;
      this.level = level;
    }
  mostrarInfo (){
    return this.name + this.level
  }
}