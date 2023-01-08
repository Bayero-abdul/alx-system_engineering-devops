# What happens when you type google.com in your browser and press Enter?


Before we dive deep in lets define some terms that will give us a better understanding of how everything works:

* **Internet** - the Internet is a vast network that connects computers all over the world.

* **Internet Service Provider (ISP)** - an organization that provides services for accessing, using, or participating in the Internet.

* **Client** - the user-agent; any tool that acts on behalf of the user. This role is primarily performed by the Web browser, but it may also be performed by programs used by engineers and Web developers to debug their applications.

* **Client requests** - queries sent to the server by the client.

* **Resolver** - a set of dynamic library routines used by applications that need to know machine names.

* **Server** - a piece of computer hardware or software that provides functionality for other programs or devices, called "clients".

* **Webserver** - is computer software with underlying hardware that connects to the Internet and supports physical data interchange with other devices connected to the web.

* **Domain Name System (DNS)** - the hierarchical and decentralized naming system used to identify computers, services, and other resources reachable through the Internet or other Internet Protocol networks.

* **Internet Protocol address (IP)** - a numerical label such as 192.0.2.1 that is connected to a computer network that uses the Internet Protocol for communication. An IP address serves two main functions: network interface identification and location addressing.

* **Transmission Control Protocol (TCP)** - a connection-oriented protocol that means it establishes the connection before the communication that occurs between the computing devices in a network. This protocol is used with an IP protocol, so together, they are referred to as a TCP/IP.

* **HyperText Transfer Protocol (HTTP)** - a protocol for fetching resources such as HTML documents. It is the foundation of any data exchange on the Web and it is a client-server protocol, which means requests are initiated by the recipient, usually the Web browser.

* **Load balancer** - a device/program that acts as a reverse proxy and distributes network or application traffic across many servers.

* **Application server** - a type of server designed to install, operate and host-associated services and applications for the IT services, end-users and organizations.

* **Database** - is an organized collection of structured information, or data, typically stored electronically in a computer system.

* Firewall** - a network security system that monitors and controls the incoming and outgoing network traffic based on predetermined security rules.


Your computer sends a request to Google's servers when you type google.com into your browser and press Enter. The information that makes up the Google homepage is then sent back by Google's servers. After rendering the data, your browser creates a webpage for you to view.


## 1. Introduction.

Your browser will direct you to the Google home page when you type "google.com" and press Enter. You can look up information on the internet using Google as a search engine.


## 2. what happens after you enter www.google.com into your browser.

When you type a web address into your browser, your computer contacts the DNS server associated with your internet service provider and requests the IP address for the web server associated with the web address you entered. Once it has the IP address, your computer contacts the web server and requests the web page you want to see.

The web server sends the web page to your browser, and the browser begins rendering the page. Depending on how the page is designed, your browser may need to make additional requests to other web servers to fetch additional resources required to render the page, such as style sheets, images, and JavaScript files.

Once the browser has received all the resources it needs, it displays the web page.


## 3. the procedure of a web page loading.

how your browser displays the website.

Your browser contacts a DNS server to resolve a web address into an IP address when you type it into the address bar and press enter. When your browser has the IP address, it will then use that address to get in touch with the web server and ask for the requested webpage.

Your browser will then receive the HTML code for the web page from the web server. In accordance with the HTML code, the browser will then render the website.

The CSS code used to style the website is also transmitted from the web server to the browser. A web page's interactivity is added using JavaScript code, which is also sent from the web server.

The web server also sends other files, such as images, videos, and other files, which are used to add multimedia to the website.

The web page is displayed in your browser once all of the files have been received.


## 4. How a web server and your browser interact.

A web server begins to operate as soon as a browser sends a request to it. Prior to beginning to respond, it must first comprehend the request.

The server first verifies the URL that the browser has requested. After that, it must locate the actual file matching that URL on the server. For instance, the server will look for a file named about.html if the URL is http://example . com/about.

The file will be located by the server, read, and its contents sent back to the browser. The user will then see the page rendered by the browser.

The server will notify the browser of an error if it cannot locate the file.

The entire process happens very quickly, and frequently the user won't even notice it.


## 5. how a web server handles a request.

Any time you enter a web address into your browser, your computer makes contact with the web server for that domain name. Your browser sends a request to the server for the particular page you want to view once your computer has located it.

The HTML code for the page you requested is then sent by the server to your browser as a response. The content is then displayed to you by your browser as it renders the page.

Your browser must understand how to communicate with web servers for this process to function. Using the Hypertext Transfer Protocol (HTTP), it accomplishes this.

Every web browser and web server utilizes the straightforward HTTP communication protocol. It lays out the formatting and transmission requirements for messages as well as the appropriate responses to different commands.

Your browser makes its first contact with the domain name server (DNS) when you type in a web address in order to determine the IP address of the web server. Once it has the IP address, it contacts the server with an HTTP request.

The server then replies with an HTTP response. Both the requested data and the request status are included in this response.

Usually, HTML code is used to transmit data from the server to the browser. The user is then presented with the web page after the browser renders this code.


## 6. how your browser displays the website.

Your browser is continuously working to load and display the pages you request as you browse the internet. Have you ever wondered what occurs in the background?

Your computer contacts a domain name server (DNS) to look up the IP address for the website you want to visit when you enter a web address into your browser. A request for the website's content is sent to the server by your computer once it has the IP address.

Following that, the server sends packets—small digital units—of the content back to your browser. Your browser starts rendering the page as the packets start to arrive.

The browser first loads any required HTML and CSS files. A web page's structure is determined by the HTML (HyperText Markup Language) and CSS (Cascading Style Sheets) codes, respectively.

To create a Document Object Model (DOM), the browser then parses the HTML and CSS files. The structure and content of the page are represented by the DOM. It also includes guidelines for how the page should look.

The browser then shows the page's contents on the screen as a final step.



## Introduction to the load balancer.

Clients don't need to know how many servers are in use or how they are configured because a load balancer intelligently distributes traffic from clients across several servers. The load balancer can improve user experience by supplying more security, performance, resilience, and making website scaling easier because it sits between the clients and the servers.

In addition to dividing traffic among servers, load balancers also carry out a variety of other tasks, such as HTTP reverse proxy, traffic and routing optimization algorithms, image caching (which lightens the load on web servers), and content caching.

Your request to view google.com will be balanced equally with all other clients' available requests. A server will be assigned to you by the load balancer.

Let's move on to something else now that you are aware of how requests are distributed among load balancers. How can you guard against unauthorized access to your website?


## introduction to firewall.

A firewall is a security tool, either hardware or software, that can help safeguard your network by filtering traffic and preventing unauthorized access to the sensitive information on your computer by outsiders.

A firewall can aid in preventing malicious software from infecting your computer in addition to blocking unwanted traffic.

Different levels of protection may be offered by firewalls. Determining how much protection you require is the key.
