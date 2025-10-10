import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { Metrics } from './modules/metrics/components/metrics/metrics';
import { SystemMonitor } from './modules/metrics/components/system-monitor/system-monitor';
import { SignupComponent } from './auth/components/signup/signup.component';
import { LoginComponent } from './auth/components/login/login.component';
import { EdgeLogin } from './auth/components/edge-login/edge-login';
import { AuthGuard } from './auth/services/auth/auth.guard';
import { MainLayoutComponent } from './modules/main-layout/main-layout.component';
const routes: Routes = [
    { path: "", 
    component: MainLayoutComponent,
    children: [
      { path: "", component: EdgeLogin },
      { path: "register", component: SignupComponent },
      { path: "login", component: EdgeLogin },
      { path: "dashboard", component: SystemMonitor, canActivate: [AuthGuard]  },
      { path: '**', redirectTo: '' }
    ] 
  },
  { path: "", component: LoginComponent },
  
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
