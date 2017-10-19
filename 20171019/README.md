1. django rest framework의 view에서 get_queryset 을 할때 None 을 반환하는 경우에 대해 예외처리가 매번 필요하다.
2. 상속개념으로는 최종적으로 정의된 get_queryset 에 대한 제어가 어렵다? 불가능하다? 복잡해진다?
3. instance decorator 또는 class decorator 를 활용한다면 한번 데코레이터를 mixin 에 정의해두고 계속해서 써먹기 좋겠네. (어 ? 열안받네?)
4. 기존 decorator 개념을 이해하고, instance, class 에 정의되는 decorator 를 다시 한번 재학습 하자
+a 클래스형태로 정의하는 데코레이터도 연습하자(함수형태랑 다를게 없으므로 pass)

