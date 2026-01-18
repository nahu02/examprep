# DOM & Event Handling: Revision Notes

## Essence of the Topic (The "Why")

**DOM manipulation** enables developers to dynamically modify web page structure, content, and styling after the page loads, transforming static HTML into interactive experiences. **Event handling** is the mechanism that responds to user interactions (clicks, hovers, etc.) by triggering programmed actions, forming the foundation of event-driven programming where program flow is controlled by user actions rather than linear execution. Together, these concepts allow developers to create responsive, engaging user interfaces that adapt to user input in real time.

## Key Concepts & Critical Vocabulary

- **Document Object Model (DOM)**: The browser's in-memory representation of the HTML document as a tree of nodes; each element responds to instructions and can be accessed, modified, or removed via JavaScript.

- **Event-Driven Programming**: A programming paradigm where the program remains idle until an event (user action or timer) triggers execution of specific code logic.

- **Event Listener**: A mechanism that monitors a DOM element for specific events (e.g., clicks, hovers) and executes a callback function when the event occurs.

- **DOM Traversal & Selection**: Methods like `querySelector()`, `getElementById()`, `getElementsByClassName()`, and `querySelectorAll()` used to locate and reference specific elements in the DOM.

- **DOM Manipulation Methods**: Core operations including `createElement()` (create nodes), `appendChild()` (add children), `innerText`/`innerHTML` (modify content), `classList` (manage classes), and `style` property (apply inline styles).

## Core Mechanism / Logical Flow

**Event-Driven Programming Cycle:**

1. **Listener Setup**: Attach an event listener to a DOM element (e.g., a button) using `addEventListener()` or inline event handlers.

2. **Event Trigger**: User interaction (click, hover, form input) generates an event that the listener detects.

3. **Event Capture & Propagation**: The event flows through the DOM tree via event bubbling (child to parent) or capturing (parent to child).

4. **Callback Execution**: The listener's callback function executes, triggering program logic (e.g., modifying content, styling, or DOM structure).

5. **DOM Update**: Changes are applied to the DOM, and the browser re-renders the affected elements.

## Critical Distinctions

| Concept | Key Difference |
|---------|---|
| **`innerText` vs `innerHTML`** | `innerText` sets/retrieves plain text content only; `innerHTML` sets/retrieves HTML markup, allowing insertion of new elements. |
| **Event Bubbling vs Capturing** | Bubbling propagates events from child to parent; capturing propagates from parent to child. Event delegation typically leverages bubbling. |
| **`querySelector()` vs `getElementById()`** | `querySelector()` is more flexible (accepts CSS selectors); `getElementById()` is faster but limited to ID selection. |
| **HTMLCollection vs NodeList** | `HTMLCollection` (returned by `getElementsByClassName()`) is live and updates automatically; `NodeList` (returned by `querySelectorAll()`) is static. |

## Exam Focus

**Probable Question Types:**

1. **Multiple-Choice (1 point each)**: Expect questions on method selection (e.g., "Which method creates a new DOM element?"), event handling syntax, and DOM traversal logic.

2. **Essay Questions (up to 6 points each)**: Likely to ask for:
   - Explanation of event-driven programming and its role in interactive UI design
   - Comparison of different DOM selection/manipulation methods and when to use each
   - Analysis of event delegation and event flow (bubbling/capturing)
   - Design of a simple interactive feature using DOM manipulation and event listeners

**Example Question:**
*"Explain how event-driven programming enables responsive user interfaces. Describe the complete flow from user interaction to DOM update, and identify two methods for attaching event listeners to DOM elements."*

**Brief Answer Summary**: Event-driven programming keeps the UI responsive by waiting for user actions rather than executing linearly. Flow: User triggers event → Listener detects event → Callback executes → Program logic modifies DOM → Browser re-renders. Two methods: (1) `addEventListener()` (recommended, allows multiple listeners), (2) inline event handlers like `onclick` (less flexible).

## Source Map

| Source | Coverage |
|--------|----------|
|  mjosh.hashnode.dev - DOM Manipulation Foundation | DOM selection methods (`querySelector`, `getElementById`, `getElementsByClassName`), element creation (`createElement`), content modification (`innerText`, `innerHTML`), event listeners, event delegation, class manipulation |
|  dev.to - Ultimate Guide to DOM Manipulation | DOM selection, content modification, event handling, styling via `element.style`, animation basics, interactivity patterns |
|  MDN - DOM Scripting Introduction | Basic DOM manipulation, node creation/placement, element removal, style manipulation |
|  The Odin Project - DOM Manipulation and Events | NodeList vs HTMLCollection distinction, three methods for event handling (inline, property assignment, event listeners) |
| **Source Material (PDF)** | IntroductionToHCI-3.pdf, Page 679 | Event-driven programming concept, event listener architecture, program flow triggered by user events |

---

**Note**: The provided search results focus on technical implementation of DOM manipulation and event handling in JavaScript. The HCI learning objectives (cognition, perception, design principles, usability evaluation) are not directly addressed in these sources. For comprehensive exam preparation, consult HCI-specific materials covering user-centered design, cognitive models, and evaluation methodologies.