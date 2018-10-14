import { Component, OnInit } from '@angular/core';
import { DbServicesService } from '../db-services.service';


@Component({
  selector: 'app-topics',
  templateUrl: './topics.component.html',
  styleUrls: ['./topics.component.css']
})
export class TopicsComponent implements OnInit {

  constructor(private authService: DbServicesService) { }
  todoLists: any;
  ngOnInit() {
  }
  allTopics() {
    this.authService.getTopics().subscribe(response => {
      this.todoLists = response;
      console.log(response);
    });
  }
}
