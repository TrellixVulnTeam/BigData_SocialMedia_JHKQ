import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {

  constructor() { }
   in: any;
   out: any;
  ngOnInit() {
  }

  GetData() {
    return null;
  }

  SendTopics(dirichlet, iterantion, topics, files) {
    console.log('Dirichlet' + dirichlet);
    console.log('Num Iter' + iterantion);
    console.log('Num Topics' + topics);
    console.log('File Name' + files);
  }


}
