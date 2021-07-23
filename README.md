# Yggdrasil
A self-modifying esoteric language based around binary trees

[Try it online!](https://tio.run/##3VjNcts2EL7zKVA3NQmLku30ptpJH6CTU24em4FJSOKUfwNSbjx18urKLkCIoABSouNeqhlbFLH77e63C2CB6rnZlMXvuzSvStGQ@rn29GMj0mLteXGZ56xIonjDRE1uie/7Z/4fNx9mF/PLh/OX5e1HeGNJZWndBDmrglIkIemNUup5jeB8L9sbBYMZq2vyGSSWHmk/CV@RKEqLtImioObZKiSiLJuQZHzVAMSnsuDwKl1v9C/aKesP6i1QDUTwyy3QIuLXAEJrRX57By4KXonWRYcHgjdbURA/@PdbSNQf9RerUuSsCfbuhZ0joWGSamr@4mwVID90lKAMxIZYwDEIwQy4F5tJFcq@LkzpqBWi9MvzEAhfR1gLAROCPYcEn@0Epis1kNZyxDbYqn3eIy2qsgquoNK0hImV1mlRN6yIeYCKoSR0OAyU8Uz9AmiRVk5XwReK6DYGAgU/BFKUCUZjBmLJSDdALFXG1NxZalVJBD7bijyr@V5OJsgtZxFncq1rxsrfiViaEVVu/w9K9NQZ4MRzlghOgpo3EcrUbTU@sazuF/@pBdsVGlsNT5bO6@el9kZGjYatiWOR9TXmVdNXdCTDjPJoGZgTwzW5wU@z6o47q520tAxPVdZNiX4i2vVXZsObVsljMegymRhET80dRbd298KQr3Ucw1XYCPbERc2DOE9qtRC/rggVsmFpW0SIaQDr/3f3hkcOB2QK6KiE3hkxhDUEvtpmWfQowM1N8LMxkHgjgv2Eot7QKO6TlMyc9lUIQ4Om9x1PkLuQ5DwvBawe8VYIXqiMhqRi@AOCT4uEf4VkXxne44In26mE38nxe@f2p8SgkVv4duQVNH1NwGElvpUBmuZVoNSJdTYVC3kZATzzz6Y6h1yOubh8CxffxpV3g67YfI/n8MaFpIpkwaoKHOxB2oGYoxjLIQFOqx/@S6uqr3aZ/eIwe4CkvcBFlXpOlO/@klg0g@p366VT/c8B9Su3tdmAuLvSYKEYqCQn@Hwa@HwS@MU08ItJ4JfTwC8vJ6E/TEN/mAR@Pg38fBL4yzTwl0FwJ/qtawLBngMGDvcny6BrE7ONOzrB/v7v3td6nYDp8Uff2eZaFA23uaez6T4YvB74WDZ@fdPYwLridlC6XRtB8O5IZxA4PKtjVsjrH2skgTZ1A0PXdjSyS5m5hv7ZpBmHU9l2hGF0qWtmtGetPSfqiCbda86PaLbxwJK@JI@Cs78HhSUnM3fLNYELsIlIY0e1tvNFMT2H7G4@kDYGesa2zcxZWrQtJhPrJ6N9XGflI8t6yoe3Hqinj369trN35Zex/DFhJF6qYz3mQmYg8uWMIqWA9oDChhHE5Bd4/5tPQwltdEsqxN5ppjtYq2vENgDvtMngLP59F91RqepSDdyQjCuyXIftEa7xdnB6O0/H5o@X4r1bwXIeRYrNCFMZRcZUlbn1fX83i6J3O3i4u17Or@/DLjUcjoEh3vIukDsYvqeU7nbXu/c/AA)


---

Yggdrasil treats its source code and its memory as the same. The memory model used by Yggdrasil is a [full binary tree](https://en.wikipedia.org/wiki/Binary_tree#Types_of_binary_trees), where each node is established initially by the source code. The characters `"';<>+*-/^&|:=?` are binary nodes, and take the next two nodes as their children. Every other character is a *leaf* node with no children. For example, `;<ab>+cd?e.` has the following binary tree:

           ;
        /     \
       /       \
      <         >
     / \     /     \  
    a   b   +       ?
           / \     /  \
          /   \   /    \
         c     d e      .
         
 Yggdrasil technically stores each character in the tree as it's Unicode code point, and treats strings as lists of code points. Before turning the source code into a tree however, Yggdrasil makes 2 substitutions:
 
- All `%` in the source code are replaced with NULL bytes
- Each `_` is replaced by the sequential command line arguments, with missing arguments filled with 0
