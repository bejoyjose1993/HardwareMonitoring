import { NgModule, provideBrowserGlobalErrorListeners } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing-module';
import { AuthModule } from './auth/auth.module';
import { App } from './app';
import { Metrics } from './modules/metrics/components/metrics/metrics';
import { HttpClientModule } from '@angular/common/http';  
import { MatToolbar } from "@angular/material/toolbar";
import { SystemMonitor } from './modules/metrics/components/system-monitor/system-monitor';

@NgModule({
  declarations: [
    App,
    Metrics,
    SystemMonitor
  ],
  imports: [
    BrowserModule,
    AuthModule,
    AppRoutingModule,
    HttpClientModule,
    MatToolbar
],
  providers: [
    provideBrowserGlobalErrorListeners()
  ],
  bootstrap: [App]
})
export class AppModule { }
