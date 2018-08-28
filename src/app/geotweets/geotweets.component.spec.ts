import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { GeotweetsComponent } from './geotweets.component';

describe('GeotweetsComponent', () => {
  let component: GeotweetsComponent;
  let fixture: ComponentFixture<GeotweetsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ GeotweetsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(GeotweetsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
