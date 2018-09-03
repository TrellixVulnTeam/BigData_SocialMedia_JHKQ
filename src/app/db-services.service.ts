import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';

const httpOptions = {
  headers: new HttpHeaders({'content-Type': 'application/json'})
};

@Injectable({
  providedIn: 'root'
})
export class DbServicesService {

  constructor(private http: HttpClient) { }

  getAuthDetails() {
    const link = '';
    return this.http.get(link);
  }

  sendAuthDetails(data) {
    const packet = [{'Details': data}];
    const body = JSON.stringify(packet);
    return this.http.post('http://127.0.0.1:5000/model', body, httpOptions);
  }

  sendTopics(files , alpha, beta, KTopics, iterate) {
    // , alpha, beta, KTopics, iterate
   // , 'alpha': alpha, 'beta': beta, 'topics': KTopics, 'iterate' : iterate}
    const packet = [{'files': files, 'alpha': alpha, 'beta': beta, 'topics': KTopics, 'iterate' : iterate}];
    const body = JSON.stringify(packet);
    return this.http.post('http://127.0.0.1:5000/model', body, httpOptions);
  }
}
