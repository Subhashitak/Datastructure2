class Node:
    def __init__(self,data,coeff,expo):
        self.data=data
        self.coeff=coeff
        self.expo=expo
def create_polynomial():
    head=None
    n=int(input("enter the size:"))
    for i in range(n):
        co=float(input("enter the co efficient:"))
        ex=int(input("enter the exponent:"))
        newnode=Node(co,ex)
        if head is None or ex>head.expo:
            newnode.next=head
            head=newnode
        else:
            temp=head
            while temp.next is not None and temp.next.expo>=ex:
                temp=temp.next
            newnode.next=temp.next
            temp.next=newnode
    return head
def addition_of_poly(poly1,poly2):
    result_head=None
    while poly1 and poly2:
        if poly1.expo>poly2.expo:
            result_head=insert_item(result_head,poly1.coeff,poly1.expo)
            poly1=poly1.next
        elif poly1.expo<poly2.expo:
            result_head=insert_item(result_head,poly2.coeff,poly2.expo)
            poly2=poly2.next
        else:
            sum_coeff=poly1.coeff+poly2.coeff
            if sum_coeff:
                result_head=insert_item(result_head,sum_coeff,poly1.expo)
            poly1=poly1.next
            poly2=poly2.next
        while poly1:
            result_head=insert_item(result_head,poly1.coeff,poly1.expo)
            poly1=poly1.next
        while poly2:
            result_head=insert_item(result_head,poly2.coeff,poly2.expo)
            poly2=poly2.next
        return result_head
def insert_item(head,coeff,expo):
    newnode=Node(coeff,expo)
    if not head or expo>head.expo:
        newnode.next=head
        head=newnode
    else:
        temp=head
        while temp.next and temp.next.expo>=expo:
            temp=temp.next
        newnode.next=temp.next
        temp.next=newnode
    return head
def display(head):
    if head is None:
        print("no polynomial")
    else:
        temp=head
        while temp is not None:
            print(f"{temp.coeff}x^{temp.expo}",end=" ")
            temp=temp.next
            if temp>0 and temp.coeff!=0:
                print("+",end=" ")
            else:
                print()
poly1=create_polynomial()
poly2=create_polynomial()
display(poly1)
display(poly2)
addition_polynomial=addition_of_poly(poly1,poly2)
display(addition_polynomial)









            
