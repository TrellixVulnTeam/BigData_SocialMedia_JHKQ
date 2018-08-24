import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AuthComponent } from './auth/auth.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { TopicsComponent } from './topics/topics.component';


const routes: Routes = [
  {path: 'index', component : AuthComponent},
  {path: 'dashboard', component : DashboardComponent},
  {path: '', redirectTo: 'index', pathMatch: 'full'},
  {path: 'topics', component : TopicsComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
