import { Component, OnInit } from '@angular/core';
import { MetricsService } from '../../services/metrics';
import { MetricsModel } from '../../models/metricsModel';
import { interval } from 'rxjs';

@Component({
  selector: 'app-system-monitor',
  standalone: false,
  templateUrl: './system-monitor.html',
  styleUrl: './system-monitor.scss'
})
export class SystemMonitor implements OnInit {
   metrics: MetricsModel | null = null;
  showRamNotification = true;
  
  constructor(private metricsService: MetricsService) {}

  ngOnInit() {
    this.fetchMetrics();
    // Refresh every 5 seconds
    interval(5000).subscribe(() => this.fetchMetrics());
  }

  fetchMetrics() {
    this.metricsService.getMetrics().subscribe(
      (data) => this.metrics = data,
      (error) => console.error('Error fetching metrics', error)
    );
  }

closeRamNotification() {
  this.showRamNotification = false;
}
}
