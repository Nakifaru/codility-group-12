def solution(A):
    all_docs = set()
    mutiple_hospital_docs = set()

    for hospital_schedule in A:
        hospital_docs = set(hospital_schedule)
        for doctor in hospital_docs:
            if doctor in all_docs:
                mutiple_hospital_docs.add(doctor)
            else:
                all_docs.add(doctor)

    print(all_docs)
    print(mutiple_hospital_docs)

    return len(mutiple_hospital_docs)


print(solution([[1,2,2], [3,1,4]]))