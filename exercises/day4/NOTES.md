# Day 4 – DRY & SOLID Refactor Notes

## DRY
**Before:** duplicated SMTP setup logic in two functions.  
**After:** extracted shared behavior into `_send_email()` so changes happen in one place.

## SRP (Single Responsibility Principle)
**Before:** `ReportService` handled both report creation and file I/O.  
**After:** split into `ReportGenerator` (business logic) and `FileReportRepository` (persistence).  
This reduces reasons-to-change per class.

## OCP (Open/Closed Principle)
**Before:** `calculate_discount` used `if/elif` branches; adding a new user type requires modifying function.  
**After:** introduced `DiscountStrategy` interface + concrete strategies; new discounts are added via new classes without modifying existing logic.

## LSP (Liskov Substitution Principle)
**Before:** `Square` inherits `Rectangle` but violates expectations of independent width/height.  
**After:** separated `Rectangle` and `Square` into independent shape types that both satisfy `Shape.area()`.

## ISP (Interface Segregation Principle)
**Before:** `Worker` forced all implementations to define `eat()` and `work()`.  
**After:** split into smaller interfaces `Workable` and `Eatable` so clients only implement what they use.

## DIP (Dependency Inversion Principle)
**Before:** `NotificationService` directly instantiated `EmailClient` (tight coupling).  
**After:** depended on abstraction (`Notifier` Protocol) and injected dependency, enabling easy testing and swapping implementations. 
