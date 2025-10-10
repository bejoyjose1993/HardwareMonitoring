import { Component, OnInit } from '@angular/core';
import { MetricsService } from '../../services/metrics';
import { MetricsModel } from '../../models/metricsModel';
import { interval } from 'rxjs';

@Component({
  selector: 'app-metrics',
  standalone: false,
  templateUrl: './metrics.html',
  styleUrl: './metrics.scss'
})
export class Metrics implements OnInit {
  metrics: MetricsModel | null = null;
  constructor(private metricsService: MetricsService) {}

  ngOnInit() {
    this.fetchMetrics();
    // Auto-refresh every 5 seconds
    interval(5000).subscribe(() => this.fetchMetrics());
  }

  fetchMetrics() {
    this.metricsService.getMetrics().subscribe(
      (data) => this.metrics = data,
      (error) => console.error('Error fetching metrics', error)
    );
  }

}
