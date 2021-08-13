import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  tags:string = "";
  allTags: string[] = [];

  createTag(event: { keyCode: number; }){
    if (event.keyCode === 13 || event.keyCode === 44) {
      this.allTags.push(this.tags);
      this.tags = ''
    }
  }

  deleteTag(index: any) {  
    this.allTags.splice(index, 1);  
  }

}
