import { Component, OnInit } from '@angular/core';
import { DbServicesService } from '../db-services.service';


@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {

  constructor(private authService: DbServicesService) { }
   in: any;
   out: any;
   myData: any;
  ngOnInit() {
  }

  SendTopics(alpha, beta, iterate, topics, files) {
    this.authService.sendTopics(files, alpha, beta, topics, iterate).subscribe(
      response => sessionStorage.setItem('value', String(response)),


      err => console.log(err),
    );
  }

  todolistFormSubmit(data) {
    console.log( sessionStorage.getItem('value'));
  }
}
