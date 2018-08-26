import { Component, OnInit } from '@angular/core';
import { DbServicesService } from '../db-services.service';

@Component({
  selector: 'app-auth',
  templateUrl: './auth.component.html',
  styleUrls: ['./auth.component.css']
})
export class AuthComponent implements OnInit {
  myData: any;
  constructor(private authService: DbServicesService) { }

  ngOnInit() {
  }
  PullData() {
    this.authService.getAuthDetails().subscribe(response => {
      this.myData = response;
    });
  }
  SendData(all: any) {
    this.authService.sendAuthDetails(all).subscribe(
      response => console.log(response),
      err => console.log(err)
    );
  }
}
