import java.util.Iterator;

public class LinkedList<E> implements Iterable<E> {
    class Node<E> {
        E data;
        Node<E> next;

        public Node(E obj) {
            data = obj;
            next = null;
        }
    }

    private Node<E> head;
    private int currentSize;

    public LinkedList() {
        head = null;
        currentSize = 0;
    }

    public void addFirst(E obj) {
        Node<E> node = new Node<E>(obj);
        node.next = head;
        head = node;
        currentSize++;
    }

    public void addLast(E obj) {
        Node<E> node = new Node<E>(obj);
        if (head == null) {
            head = node;
            currentSize++;
            return;
        }

        Node<E> temp = head;
        while (temp.next != null) {
            temp = temp.next;
        }

        temp.next = node;
        currentSize++;
    }

    public E removeFirst() {
        if (head == null) {
            return null;
        }

        E temp = head.data;
        head = head.next;
        currentSize--;
        return temp;
    }

    public E removeLast() {
        if (head == null) {
            return null;
        }

        Node<E> prev = null;
        Node<E> current = head;

        while (current.next != null) {
            prev = current;
            current = current.next;
        }

        E temp = current.data;
        prev.next = null;
        return temp;
    }

    public E remove(E obj) {
        Node<E> current = head;
        Node<E> prev = null;
        while (current != null) {
            if (((Comparable<E>) current.data).compareTo(obj) == 0) {
                if (current == head) {
                    return removeFirst();
                }
                if (current.next == null) {
                    return removeLast();
                }
                currentSize--;
                prev.next = current.next;
                return current.data;
            }
            prev = current;
            current = current.next;
        }
        return null;
    }

    public boolean contains(E obj) {
        Node<E> current = head;
        Node<E> prev = null;
        while (current != null) {
            if (((Comparable<E>) current.data).compareTo(obj) == 0) {
                return true;
            }
            prev = current;
            current = current.next;
        }
        return false;
    }

    public E peekFirst() {
        if (head == null) {
            return null;
        }

        return head.data;
    }

    public E peekLast() {
        Node<E> current = head;
        Node<E> prev = null;

        while (current != null) {
            prev = current;
            current = current.next;
        }

        return prev.data;
    }

    public Iterator<E> iterator() {
        return new Iterator<E>() {
            Node<E> current = head;

            @Override
            public boolean hasNext() {
                return current != null;
            }

            @Override
            public E next() {
                if (hasNext()) {
                    E data = current.data;
                    current = current.next;
                    return data;
                }
                return null;
            }
        };
    }

    public static void main(String[] args) {
        LinkedList<Integer> list = new LinkedList<Integer>();

        int n = 10;
        for (int i = 0; i < n; i++) {
            list.addLast(i);
        }

        list.remove(5);

        for (int i : list) {
            System.out.println(i);
        }

    }

}