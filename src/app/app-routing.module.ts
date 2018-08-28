import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AuthComponent } from './auth/auth.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { TopicsComponent } from './topics/topics.component';
import { SentimentComponent } from './sentiment/sentiment.component';
import { GeotweetsComponent } from './geotweets/geotweets.component';


const routes: Routes = [
  {path: 'index', component : AuthComponent},
  {path: 'dashboard', component : DashboardComponent},
  {path: '', redirectTo: 'index', pathMatch: 'full'},
  {path: 'topics', component : TopicsComponent},
  {path: 'sentiment', component : SentimentComponent},
  {path: 'geotweets', component : GeotweetsComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
